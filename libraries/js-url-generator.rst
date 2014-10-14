==============
JsUrlGenerator
==============

Консольная команда, предназначенная для генерации javascript url генератора.

Использование
-------------

.. code-block:: php

    <?php
    // providers.php
    return [
        "\\Vermillion\\JsUrlGenerator\\Provider" => [
            // Путь к сгенерированному файлу
            'js_url_generator.path' => __DIR__ . '/../../public/assets/js/url-generator.js',
        ],
    ];

Для того чтобы сгенерировать файл, необходимо выполнить ``bin/console js-url-generator:dump``

У этой команды имеются следующие опции:

- ``--base-path`` - Базовый путь к публичному директорию (по умолчанию пустая строка).
- ``--object`` - Имя javascript объекта (по умолчанию ``URLGenerator``).

Пример генерации путей с помощью полученного генератора:

.. code-block:: javascript

    var url = URLGenerator.generate('route_name'); // /some/path
    var url = URLGenerator.generate('route_name', {param: 'value'}); // /another/path/value
