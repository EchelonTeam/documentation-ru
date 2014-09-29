Response Factory
===========================

Эта библиотека позволяет конвертировать результаты работы контроллера в объекты класса `\\Symfony\\Component\\HttpFoundation\\Response`.

Её можно использовать независимо от фреймворка при условии, что вы используете следующие компоненты:

- `Symfony/HttpFoundation`
- `Symfony/HttpKernel`
- `Symfony/EventDispatcher`

Установка
---------

.. code-block:: sh

    $ composer require vermillion/response-factory

Регистрация
-------------

Добавьте `\\Vermillion\\Provider\\ResponseFactory\\Provider` в `providers.php`:

**Опции:**

- `response_factory.request_key` - Имя атрибута запроса для получения имени обработчика
- `response_factory.priority` - Приоритет для обработчика события ответа от контроллера
- `response_factory.handlers` - Список обработчиков (json доступен по умолчанию)
- `response_factory.default_handler` - Обработчик, используемый по умолчанию, если атрибут не указан.

Вы так же можете определить свой обработчик:

.. code-block:: php

    <?php
    // providers.php
    return [
        '\\Vermillion\\Provider\\ResponseFactory\\Provider' => [
            'response_factory.handlers' => function () {
                return [
                    'json' => new JsonHandler(),
                    'custom' => new CustomHandler(),
                ]
            }
        ]
    ]

Но помните, что создание экземпляров классов в конфигурационном файле не рекомендуется и для этого лучше использовать провайдер.

Если вы не используете Vermillion, то вам нужно будет проделать следующее:

.. code-block:: php

    <?php
    use Symfony\Component\EventDispatcher\EventDispatcher;
    use Vermillion\ResponseFactory\ControllerResponseListener;
    use Vermillion\ResponseFactory\HandlerCollection;
    use Vermillion\ResponseFactory\JsonHandler;
    
    // Определить обработчики, которые будут заниматься 
    // созданием ответов на основе результатов контроллеров
    $handlers = ['handler_name' => new JsonHandler()];

    // Создать коллекцию и обработчик события ответа от контроллера.
    // А так же зарегистрировать обработчик в диспетчере.

    $collection = new HandlerCollection($handlers);
    $priority = 256; // Приоритет для обработчика события ответа от контроллера
    $requestKey = '_handler'; // Имя атрибута запроса для получения имени обработчика
    $defaultHandler = null; // Имя обработчика, используемого по умолчанию
    $listener = new ControllerResponseListener($collection, $requestKey, $priority, $defaultHandler);
    $eventDispatcher = new EventDispatcher();
    $eventDispatcher->addSubscriber($listener);

Использование
---------------

Если вы используете Router из компонента `Symfony/Routing`, то вы можете определить имя обработчика в конфигурационном файле:

.. code-block:: yaml

    name:
        path: /
        defaults: {_controller: controller, _handler: handler_name}

В противном случае вам нужно будет найти любой другой способ, который позволит установить имя обработчика в атрибуты запроса.

При создании собственного обработчика вы должны унаследоваться от `\\Vermillion\\ResponseFactory\\AbstractResponseHandler` или реализовать `\\Vermillion\\ResponseFactory\\HandlerInterface`

Использование `AbstractResponseHandler` позволит вам указывать в ответе контроллера необходимый статус и заголовки для ответа.

Предоставляемый по умолчанию JsonHandler является наследником `AbstractResponseHandler`.

Значение, возвращаемое контроллером должно быть массивом.
При использовании `AbstractResponseHandler` в массиве могут быть следующие элементы:

- `_status` - Статус ответа.
- `_headers` - Массив заголовков ответа.

Пример:

.. code-block:: php

    <?php
    // Метод какого-либо контроллера
    public function greet($name) 
    {
        if ($name == 'non-existent') {
            return ['_status' => 404, 'message' => 'User does not exists'];
        }
        return ['message' => sprintf('Hello, %s!', $name)];
    }
    
.. code-block:: yaml

    # routing.yml 
    name:
        path: /greet/{name}
        defaults: {_controller: controller:greet, _handler: json}
