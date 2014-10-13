Configuration
=============

Предоставляет компонент `Symfony/Config <https://github.com/symfony/config>`_.

Использование
-------------

Провайдер уже зарегистрирован по умолчанию.

Для загрузки конфигурационного файла воспользуйтесь сервисом `config`, который является экземпляром класса, реализующего `\\Symfony\\Component\\Config\\Loader\\LoaderInterface`.

.. code-block:: php

    <?php
    $pimple['config']->load('config.php');

Поддерживаемые типы файлов: `yaml`, `php`, `json`

Для более подробной информации обратитесь к `документации <http://symfony.com/doc/current/components/config/index.html>`_ компонента.