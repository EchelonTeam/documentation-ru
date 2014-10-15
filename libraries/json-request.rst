======================
JsonRequest Middleware
======================

Добавляет поддержу application/json запросов.

Когда клиент присылает запрос с заголовком Content-Type: application/json,
по умолчанию нет возможности использовать
`ParameterBag <http://api.symfony.com/2.5/Symfony/Component/HttpFoundation/ParameterBag.html>`_.

JsonRequest Middleware решает эту проблему.
Достаточно просто добавить ``\\Vermillion\\JsonRequest\\Provider`` в ``providers.php``.

Пример.

До:

.. code-block:: php

    <?php
    $data = json_decode($request->getContent(), true);
    $name = isset($data['name']) ? $data['name'] : null;

После:

.. code-block:: php

    <?php
    $name = $request->request->get('name');
