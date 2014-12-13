Captcha Provider
================

Добавляет поддержку капчи с помощью `Gregwar/Captcha <https://github.com/gregwar/captcha>`_

Использование
-------------

В ``composer.json`` необходимо добавить: ``"gregwar/captcha": "~1.0"``

Добавьте ``\Vermillion\Captcha\Provider`` в ``providers.php``.

Для его работы также необходимо зарегистрировать ``\Vermillion\Session\Provider``.

Отредактируйте ``routing.yml``:

.. code-block:: yaml

    captcha:
      path: /captcha
      defaults: {_controller: captcha:show}
      requirements: {_method: GET}

Для проверки правильности пользовательского ввода вы можете использовать
функцию ``captcha.test``, которая зарегистрирована в контейнере:

.. code-block:: php

    <?php
    $pimple['captcha.test']($request->get('captcha')); // true or false

Опции
-----

.. code-block:: php

    <?php
    'captcha.options' = [
        'session_key'   => 'gw_captcha', // Имя ключа для проверочного кода, который хранится в сессии
        'width'         => 150,
        'height'        => 40,
        'font'          => null,
        'fingerprint'   => null,
        'quality'       => 90,
        'distortion'    => true,
        'background'    => [250, 0, 0],
        'interpolation' => true
    ];


Для получения более подробной информации обратитесь к `API <https://github.com/gregwar/captcha#api>`_ библиотеки.
