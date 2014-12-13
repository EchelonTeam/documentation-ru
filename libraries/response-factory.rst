Response Factory
================

Эта библиотека позволяет конвертировать результаты работы контроллера
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

    name:
        path: /
        defaults: {_controller: controller, _handler: handler_name}

При создании собственного обработчика вы должны унаследоваться
от ``\Vermillion\ResponseFactory\AbstractResponseHandler``
или реализовать ``\Vermillion\ResponseFactory\HandlerInterface``

Использование ``AbstractResponseHandler`` позволит вам указывать в ответе
контроллера необходимый статус и заголовки для ответа.

По умолчанию доступны обработчики, позволяющие конвертировать ответы контроллеров в JSON или HTML.
Оба обработчика являются наследниками ``AbstractResponseHandler``.

HTML обработчик регистрируется только при условии, что зарегистрирован провайдер для ``Plates``.

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
    html:
        path: /html
        defaults: {_controller: controller:html, _handler: plates, _template: main::template}

Для первого маршрута возвращаемое значение метода greet будет сконвертировано в JsonResponse.

Возвращаемое значение метода html будет передано объекту шаблонизатора.
Атрибут _template определяет `имя шаблона <http://platesphp.com/engine/folders/>`_, который необходимо использовать.

При использовании html обработчика метод контроллёра обязательно должен возвращать массив.
