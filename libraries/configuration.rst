Configuration
=============

Предоставляет компонент `Symfony/Config <https://github.com/symfony/config>`_.

Использование
-------------

Провайдер уже зарегистрирован по умолчанию.

Для загрузки конфигурационного файла воспользуйтесь сервисом ``config``, который
является экземпляром класса, реализующего ``\Symfony\Component\Config\Loader\LoaderInterface``.

.. code-block:: php

    <?php
    $pimple['config']->load('config.php');

Поддерживаемые типы файлов: ``yaml``, ``php``, ``json``

При загрузке конфигурационного файла будет проверяться наличие локального конфига.
Если он существует, то параметры, описанные в нём, переопределят параметры оригинального конфига.

Пример:

.. code-block:: php

    <?php
    // config.php
    return [
        'key' => 'value',
        'customized' => 'default',
        'nested' => [
            'k1' => 'v1',
            'k2' => 'v2',
        ],
    ];

.. code-block:: php

    <?php
    // config.php.local
    return [
        'customized' => 'user',
        'nested' => [
            'k2' => 'v2local',
        ],
    ];


Вызов ``$pimple['config']->load('config.php');`` вернёт массив со следующим содержимым:

.. code-block:: php

    <?php

    [
        'key' => 'value',
        'customized' => 'user',
        'nested' => [
            'k1' => 'v1',
            'k2' => 'v2local',
        ],
    ]


Для более подробной информации обратитесь
к `документации <http://symfony.com/doc/current/components/config/index.html>`_ компонента.