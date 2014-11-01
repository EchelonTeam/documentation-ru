JSON-RPC Provider
=================

Добавляет поддержку `JSON-RPC <http://www.jsonrpc.org/specification>`_
с помощью `Kilte/JSON-RPC <https://github.com/Kilte/json-rpc>`_.

Использование
-------------

Добавьте ``\Vermillion\JsonRpc\ServiceProvider`` в ``providers.php``.

Создайте класс приложения и зарегистрируйте его в контейнере под именем ``jsonrpc.user_app``:

.. code-block:: php

    <?php
    use Pimple\Container;
    use Pimple\ServiceProviderInterface;
    
    class JsonRpcAppProvider implements ServiceProviderInterface
    {
    
        public function register(Container $pimple)
        {
            $pimple['jsonrpc.user_app'] = function ($c) {
                return JsonRpcApp();
            };
        }
    
    }
    
Если вам требуется использовать JSON-RPC через HTTP, то вы можете воспользоваться контроллером,
предоставляемым провайдером по умолчанию.

Для этого необходимо добавить ``\Vermillion\JsonRpc\ControllerProvider``
в ``providers.php`` и отредактировать ``routing.yml``:

.. code-block:: yaml

    rpc:
      path: /rpc/
      defaults: {_controller: jsonrpc:rpc}
      requirements: {_method: POST}


Вы можете зарегистрировать функцию обратного вызова, которая будет выполнена перед выполнением какого-либо метода.

.. code-block:: php

    <?php
    $pimple['jsonrpc.middleware.is_admin'] = $pimple->protect(
        function (\Kilte\JsonRpc\Request\Request $request) use ($security) {
            if ($request->getMethod() == 'admin' && !$security->isGranted('ROLE_ADMIN')) {
                throw new \RuntimeException('Access denied');
            }
        }
    );
    $pimple['jsonrpc.middleware.logging'] = $pimple->protect(
        function (\Kilte\JsonRpc\Request\Request $request) use ($logger) {
            $logger->info(sprintf(
                'RPC call: %s %s %s',
                $request->getId(),
                $request->getMethod(),
                json_encode($request->getParams())
            ));
        }
    );


По умолчанию доступен AccessControlMiddleware, который позволяет осуществить настройку доступа
с использованием конфигурационного файла.

Для его использования необходимо:

- зарегистрировать и настроить ``\Vermillion\Security\Provider``.
- создать конфигурационный файл ``jsonrpc.yml``, определив в нём параметры доступа.

Пример конфигурационного файла:

.. code-block:: yaml

    access_map:
      admin.user.edit: ROLE_ADMIN
      admin.user.remove: ROLE_ADMIN
      user.profile: ROLE_USER
      another.method: [ROLE_ONE, ROLE_TWO]
    exception:
        access_denied: -32001

В секции ``exception`` определяются коды ошибок.
``access_denied`` используется в ``AccessControlMiddleware`` и предназначен для определения кода ошибки,
если доступ к методу запрещён.

Код ошибки должен находиться в диапазоне между `-32000 и -32099 <http://www.jsonrpc.org/specification#error_object>`_.


Для более подробной информации обратитесь к документации библиотеки.
