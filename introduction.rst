========
Введение
========

Установка
=========
Рекомендуемый метод установки - через Composer_, указав `"vermillion/vermillion": "dev-master"` в списке зависимостей. 

.. note:: 
    Вместо dev-master следует указать текущую стабильную версию. 
    Узнать её можно, например `здесь <https://packagist.org/packages/vermillion/vermillion>`_

Создание первого приложения
===========================

Для того, чтобы загрузить фреймворк, необходимо подключить `vendor/autoload.php` и создать экземпляр класса `\\Vermillion\\General\\Application`:

.. code-block:: php

    // public/index.php
    require __DIR__ . '/../vendor/autoload.php';
    $app = new \Vermillion\General\Application(__DIR__ . '/../config');
    $app->run();

Конструктор класса в качестве первого аргумента принимает путь к директорию с конфигурационными файлами.
Вторым аргументом можно передать экземпляр класса `\\Pimple\\Container`.

Для того, чтобы запустить приложение, необходимо вызвать метод `run()`, который может принимать объект класса `\\Symfony\\HttpFoundation\\Request`. 
По умолчанию он будет создан на основе глобальных переменных.


Чтобы заставить наше приложение работать, необходимо создать файл `providers.php` в директории, указанном приложению, при создании экземпляра класса `\\Vermillion\\General\\Application`.

.. code-block:: php

    // public/../config/providers.php
    return [
        "\\ControllerProvider"
    ];

Этот файл должен вернуть массив доступных для регистрации провайдеров.
Имя провайдера, как вы уже наверное догадались, определяется полным именем класса.

Вы также можете указать опции для этого провайдера, если он реализует `\\Pimple\\ServiceProviderInterface`:

.. code-block:: php

    return [
        '\\SomeServiceProvider' => [
            'one_option' => 'value',
            'another_option' => 'another_value'
        ]
    ];

Можно даже использовать возможности Pimple и создавать службы:

.. code-block:: php

    return [
        '\\SomeServiceProvider' => [
            'service' => function ($c) {
                return new SomeService($c['another_service'])
            }
        ]
    ];

Но не следует делать такие вещи. Вместо этого лучше использовать провайдеры.


Перейдём к контроллёрам. 

Так как это всего-лишь пример, то создайте файл `controllers.php` и подключите его в `public/index.php`.
В реальных проектах этого делать не следует.

.. code-block:: php

    // controllers.php
    use Pimple\Container;
    use Symfony\Component\HttpFoundation\Response;
    use Vermillion\General\Api\ControllerProviderInterface;
    
    class ControllerProvider implements ControllerProviderInterface
    {
    
        public function registerControllers(Container $controllers, Container $pimple)
        {
            $controllers['controller'] = function () {
                return new Controller();
            };
        }
    }
    
    class Controller
    {
    
        public function hello()
        {
            return new Response('Hello!');
        }
    
    }


Здесь мы определили сам контроллер и провайдер для него.

Теперь нужно сказать фреймворку, что мы хотим, чтобы метод `Controller::hello()`, вызывался, когда мы обращаемся к домашней странице нашего приложения. 

Для этого необходимо создать файл `routing.yml` и расположить его рядом с `providers.php`:

.. code-block:: yaml

    home:
      path: /
      defaults: {_controller: controller:hello}

Здесь в качестве контроллера указано имя контроллера, которое использовалось при регистрации его в контейнере и через двоеточие имя метода, который должен быть вызван.

Для более подробного описания маршрутизации смотрите документацию к `Symfony/Routing <http://symfony.com/doc/current/components/routing/introduction.html>`_.

Теперь выполните `php -S localhost:8080` в директории с `index.php` и откройте в браузере `http://localhost:8080/index.php`

Если вы всё сделали правильно, то вы должны увидеть страницу с текстом "Hello!"

.. _Composer: http://getcomposer.org