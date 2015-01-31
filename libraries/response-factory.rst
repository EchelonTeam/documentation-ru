Response Factory
================

Эта библиотека позволяет конвертировать значения, возвращаемые методами контроллеров,
в объекты класса ``\Symfony\Component\HttpFoundation\Response``.

Регистрация
-----------

Добавьте ``\\Vermillion\\ResponseFactory\\Provider`` в ``providers.php``:

**Опции:**

- ``response_factory.request_key`` - Имя атрибута запроса для получения имени обработчика
- ``response_factory.priority`` - Приоритет для обработчика события ответа от контроллера
- ``response_factory.handlers`` - Список обработчиков (json доступен по умолчанию)
- ``response_factory.default_handler`` - Обработчик, используемый по умолчанию, если атрибут не указан.

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

Использование
-------------

Определить имя обработчика в конфигурационном файле:

.. code-block:: yaml

    # routing.yml
    name:
        path: /
        defaults: {_controller: controller, _handler: handler_name}

При создании собственного обработчика вы должны унаследоваться
от ``\Vermillion\ResponseFactory\AbstractResponseHandler``
или реализовать ``\Vermillion\ResponseFactory\HandlerInterface``

Использование ``AbstractResponseHandler`` позволит вам указывать в ответе
контроллера необходимый статус и заголовки для ответа.

При использовании ``AbstractResponseHandler``, если контроллёр возвращает массив, то в нём могут быть следующие элементы:

- ``_status`` - Статус ответа.
- ``_headers`` - Массив заголовков ответа.

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
