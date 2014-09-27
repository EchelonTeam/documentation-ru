Security/Core Provider
=================================

Предоставляет `Symfony/Security-Core <http://symfony.com/doc/current/components/security/index.html>`_ компонент для `Pimple <https://github.com/fabpot/Pimple>`_ и может быть использован независимо от фреймворка.

Установка
---------

.. code-block:: sh

    $ composer require vermillion/security-core-provider

Использование
--------------

.. code-block:: php

    use Pimple\Container;
    use Vermillion\Provider\Security\SecurityCoreProvider;
    
    $c = new Container();
    $options = [
        // Скрывать ли исключения при аутентификации 
        // Например, если пользователь не найден или неверно указан пароль, то 
        // будет выброшено исключение с соответствующим сообщением.
        // Эта опция позволяет заменить подобные сообщения на одно единественное сообщение 
        // вроде "Bad credentials"
        'security.options.hide_user_not_found' => false,
        // Уникальный ключ для RememberMeAuthenticationProvider
        'security.options.remember_me_key'     => 'C3nJqYZg3m9sFvWt0OSmNk8mZipHj6wRMSwk0yaLpR4Tf0izSTmF95TB5Ec6',
        // Пользователи для InMemoryUserProvider
        // Если провайдер пользователей переопределён, 
        // то изменение этой опции не будет ни на что влиять.
        'security.users'                       => [
            'username' => [
                // 123456
                'password' => 'zKgdNE7BHguhCKv+42U0WnRCbF8DgMJRQCi2aqzk3vMGfP0ZNIIes6SK+aE6cZtlVm4rEKfY4earvqcNGIMuSA=='
            ]
        ]
    ];
    $c->register(new SecurityCoreProvider(), $options);
    if ($c['security']->isGranted('ROLE_ADMIN')) {
        // ...
    }

Если необходимо переопределить провайдер пользователей:

.. code-block:: php

    use Pimple\Container;
    use Vermillion\Provider\Security\SecurityCoreProvider;
    
    $c = new Container();
    $options['security.user.provider'] = function ($c) {
        return new CustomUserProvider($c['required_service']);
    };
    $c->register(new SecurityCoreProvider(), $options);

Для более подробной информации обратитесь к документации компонента.
