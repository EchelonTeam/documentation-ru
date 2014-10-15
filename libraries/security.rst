Security Provider
=================

Предоставляет `Symfony/Security-Core <https://github.com/symfony/security-core>`_ компонент.

Использование
-------------

Добавьте ``\Vermillion\Security\Provider`` в ``providers.php``:

.. code-block:: php

    <?php
    return [
        "\\Vermillion\\Security\\Provider" => [
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
        ]
    ];


``SecurityContext`` доступен как security сервис:

.. code-block:: php

    <?php
    $c->register(new SecurityCoreProvider(), $options);
    if ($c['security']->isGranted('ROLE_ADMIN')) {
        // ...
    }

Если необходимо переопределить провайдер пользователей, то нужно заменить службу ``security.user.provider``:

.. code-block:: php

    <?php
    use Pimple\Container;
    use Pimple\ServiceProviderInterface;

    class ServiceProvider implements ServiceProviderInterface
    {

        public function register(Container $pimple)
        {
            $pimple['security.user.provider'] = function ($c) {
                return new CustomUserProvider($c['required_service']);
            };
        }

    }

Для более подробной информации обратитесь к документации компонента.
