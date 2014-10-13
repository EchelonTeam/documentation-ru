Plates Provider
===============

Добавляет поддержку шаблонов с помощью `Plates <http://platesphp.com>`_.

Установка
---------

.. code-block:: sh

    $ composer require vermillion/plates-provider

Использование
-------------

Добавьте `\\Vermillion\\Provider\\Plates\\Provider` в `providers.php`.

**Опции:**

- `plates.options.paths` - Список доступных `директорий <http://platesphp.com/engine/folders/>`_
- `plates.options.extension` - `Расширение файла шаблона <http://platesphp.com/engine/file-extensions/>`_ (`php` по умолчанию)
- `plates.options.ext.uri` - Параметр для `URI расширения <http://platesphp.com/extensions/uri/>`_
- `plates.options.ext.asset.path` - Путь к директорию для `Asset расширения <http://platesphp.com/extensions/asset/>`_
- `plates.options.ext.asset.filename_method` - Метод кеширования файла для Asset расширения (false по умолчнанию)

Регистрация:

.. code-block:: php

    <?php
    // providers.php
    return [
        "\\Vermillion\\Provider\\Plates\\Provider" => [
            'plates.options.paths' => [
                // name, directory, fallback (false by default)
                ['main', $resources . 'views/'],
                ['pages', $resources . 'views/pages/']
            ],
            'plates.options.ext.asset.path' => __DIR__ . '/../../public/'
        ],
    ];


Экземпяр класса `Engine` зарегистрирован как `plates`:

.. code-block:: php
    
    <?php
    $pimple['plates']->render('directory::template', []);

Вы можете использовать функцию `url()` в ваших шаблонах для того, чтобы сгенерировать URL, используя `Symfony/Routing <http://symfony.com/doc/current/components/routing/introduction.html>`_ компонент.

Для того, чтобы добавить своё расширение, просто зарегистрируйте службу с именем, начинающимся с `plates.ext.`

Для более подробной информации смотрите документацию `библиотеки <http://platesphp.com>`_.