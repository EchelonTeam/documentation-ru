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
    
Для более подробной информации обратитесь к документации библиотеки.

Если вам требуется использовать JSON-RPC через HTTP, то вы можете воспользоваться контроллером, предоставляемым провайдером по умолчанию.

Для этого необходимо добавить `\\Vermillion\\Provider\\JsonRpc\\ControllerProvider` в `providers.php` и отредактировать `routing.yml`:

.. code-block:: yaml

    rpc:
      path: /rpc/
      defaults: {_controller: jsonrpc:rpc}
      requirements: {_method: POST}
