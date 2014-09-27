Configuration
=============

Предоставляет компонент `Symfony/Config <https://github.com/symfony/config>`_ для `Pimple <https://github.com/fabpot/Pimple>`_ и может использоваться независимо от фреймворка.

Установка
---------

.. code-block:: sh

    $ composer require vermillion/config

Использование
--------------

Поддерживаемые типы файлов: `yaml`, `php`, `json`

**Опции:**

- `config.paths` - Путь к директорию с конфигурационными файлами. Может быть как массивом, так и строкой.

Для того, чтобы получить доступ к службе, зарегистрируйте провайдер в `providers.php`:

.. code-block:: php
    
    // providers.php
    return [
        '\Vermillion\Config\Provider' => [
            'config.paths' => [__DIR__ . '/prod', __DIR__ . '/dev', __DIR__ . '/default']
        ]
    ];

Если вы хотите использовать провайдер независимо от фреймворка, то можете вручную зарегистрировать его в контейнере:

.. code-block:: php

    $c = new \Pimple\Container();
    $c->register(new \Vermillion\Config\Provider(), ['config.paths' => __DIR__ . '/config']);
    $config = $c['config']->load('config.yml');
    

Для более подробной информации обратитесь к `документации <http://symfony.com/doc/current/components/config/index.html>`_ компонента.