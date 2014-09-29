Расширение фреймворка
=====================

Трудно не согласиться с тем, что сам по себе фреймворк мало чем полезен.
Но эта проблема легко решается с помощью сторонних библиотек и провайдеров для них.

Vermillion предлагает некоторые уже готовые решения. 
Все они доступны на Packagist_, что позволяет установить их с помощью Composer_.
Вам остаётся только указать библиотеку в зависимостях проекта, добавить провайдер в `providers.php` и задать необходимые опции, если это требуется.

.. toctree::
    :maxdepth: 1
    
    libraries/index

Создание собственного провайдера
----------------------------------

Фреймворк предоставляет следующие интерфейсы для провайдеров:

- `\\Vermillion\\General\\Api\\BootableProviderInterface`
- `\\Vermillion\\General\\Api\\ControllerProviderInterface`
- `\\Vermillion\\General\Api\\EventListenerProviderInterface`
- `\\Vermillion\\General\\Api\\MiddlewareProviderInterface`

BootableProviderInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~

- `void onBoot(\\Pimple\\Container $pimple)`

`onBoot()` вызывается во время вызова метода `\\Vermillion\\General\\Application::boot()`,
после того, как все провайдеры были зарегистрированы.

Вы можете использовать его для того, чтобы получить прямой доступ к службам, зарегистрированным в контейнере.

Смотрите документацию к Pimple_ для более подробной информации.

ControllerProviderInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `void registerControllers(\\Pimple\\Container $controllers, \\Pimple\\Container $pimple);`

Используется для регистрации контроллеров в контейнере (`$controllers`).

EventListenerProviderInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `void registerListeners(\\Symfony\\Component\\EventDispatcher\\EventDispatcherInterface $dispatcher, \\Pimple\\Container $pimple)`

Предназначен для регистрации обработчиков событий в диспетчере.

MiddlewareProviderInterface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `\Symfony\Component\HttpKernel\HttpKernelInterface wrap(\\Symfony\\Component\\HttpKernel\\HttpKernelInterface $kernel, \\Pimple\\Container $pimple)`

Используется для регистрации `middleware`.

Middleware представляет собой класс, реализующий `HttpKernelInterface`
Его конструктор должен принять объект, реализующий `HttpKernelInterface`,
а метод handle делегировать вызов принятому в конструкторе объекту.

Пример:

.. code-block:: php

    use Pimple\Container;
    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\HttpFoundation\Response;
    use Symfony\Component\HttpFoundation\Session\Session;
    use Symfony\Component\HttpKernel\HttpKernelInterface;
    use Symfony\Component\HttpKernel\TerminableInterface;
    use Vermillion\General\Api\MiddlewareProviderInterface;
    
    class SessionMiddlewareProvider implements MiddlewareProviderInterface
    {
    
        public function wrap(HttpKernelInterface $kernel, Container $pimple)
        {
            return new SessionMiddleware($kernel);
        }
    
    }
    
    class SessionMiddleware implements HttpKernelInterface, TerminableInterface
    {
    
        private $kernel;
    
        public function __construct(HttpKernelInterface $kernel)
        {
            $this->kernel = $kernel;
        }
    
    
        public function handle(Request $request, $type = self::MASTER_REQUEST, $catch = true)
        {
            $request->setSession(new Session());
            return $this->kernel->handle($request, $type, $catch);
        }
    
        public function terminate(Request $request, Response $response)
        {
            // Вы также можете реализовать TerminableInterface, но в этом случае делегировать вызов метода не нужно.
        }
    
    }

Провайдеры служб
~~~~~~~~~~~~~~~~

Все приведённые выше интерфейсы позволяют получить доступ к контейнеру,
содержащему службы через соответствующий аргумент метода (`$pimple`)

Для провайдеров служб используйте `\\Pimple\\ServiceProviderInterface`

.. _Composer: http://getcomposer.org
.. _Packagist: http://packagist.org/packages/vermillion
.. _Pimple: https://github.com/fabpot/Pimple
