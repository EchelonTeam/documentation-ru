Session Provider
================

Предоставляет возможность использования сессий на основе `Symfony/HttpFoundation <http://symfony.com/doc/current/components/http_foundation/index.html>`_

Установка
---------

.. code-block:: sh

    $ composer require vermillion/session-provider

Использование
-------------

Добавьте `\\Vermillion\\Provider\\Session\\Provider` в `providers.php`

Для того, чтобы переопределить опции по умолчанию, вы можете зарегистрировать провайдер следующим образом:

.. code-block:: php

    <?php
    // providers.php
    return [
        '\\Vermillion\\Provider\\Session\\Provider' => [
            // Конфигурация сессии
            'session.storage.options'   => [],
            // Путь к директорию для файлов сессий
            'session.storage.save_path' => '',
        ]
    ];
