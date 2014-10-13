Session Provider
================

Предоставляет возможность использования сессий на основе `Symfony/HttpFoundation <http://symfony.com/doc/current/components/http_foundation/index.html>`_

Использование
-------------

Добавьте `\\Vermillion\\Session\\Provider` в `providers.php`

Для того, чтобы переопределить опции по умолчанию, вы можете зарегистрировать провайдер следующим образом:

.. code-block:: php

    <?php
    // providers.php
    return [
        '\\Vermillion\\Session\\Provider' => [
            // Конфигурация сессии
            'session.storage.options'   => [],
            // Путь к директорию для файлов сессий
            'session.storage.save_path' => '',
        ]
    ];
