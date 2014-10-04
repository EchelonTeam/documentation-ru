JSON-RPC Provider
============================

Добавляет поддержку `JSON-RPC <http://www.jsonrpc.org/specification>`_ с помощью `Kilte/JSON-RPC <https://github.com/Kilte/json-rpc>`_. 

Установка
---------

.. code-block:: sh

    $ composer require vermillion/json-rpc-provider

Использование
-------------

Добавьте `\\Vermillion\\Provider\\JsonRpc\\ServiceProvider` в `providers.php`.

Создайте класс приложения и зарегистрируйте его в контейнере под именем `jsonrpc.user_app`:

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
    
Если вам требуется использовать JSON-RPC через HTTP, то вы можете воспользоваться контроллером, предоставляемым провайдером по умолчанию.

Для этого необходимо добавить `\\Vermillion\\Provider\\JsonRpc\\ControllerProvider` в `providers.php` и отредактировать `routing.yml`:

.. code-block:: yaml

    rpc:
      path: /rpc/
      defaults: {_controller: jsonrpc:rpc}
      requirements: {_method: POST}


Вы можете зарегистрировать функцию обратного вызова, которая будет выполнена перед выполнением какого-либо метода.

.. code-block:: php

    <?php
    $pimple['jsonrpc.middlewares'] = [
        function (\Kilte\JsonRpc\Request\Request $request) use ($security) {
            if ($request->getMethod() == 'admin' && !$security->isGranted('ROLE_ADMIN')) {
                throw new \RuntimeException('Access denied');
            }
        },
        function (\Kilte\JsonRpc\Request\Request $request) use ($logger) {
            $logger->info(sprintf('RPC call: %s %s %s', $request->getId(), $request->getMethod(), json_encode($request->getParams())));
        }
    ];


Для более подробной информации обратитесь к документации библиотеки.