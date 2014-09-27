Authentication Provider
=======================

Добавляет поддержку аутентификации и является легковесной альтернативой `Symfony/Security-Http`.

Установка
---------

.. code-block:: sh

    $ composer require vermillion/authentication-provider

При установке этой библиотеки также будут установлены `vermillion/security-core-provider` и `vermillion/session-provider`. Поэтому вам потребуется сконфигурировать установленные провайдеры.

Использование
--------------

Добавьте `\\Vermillion\\Authentication\\Provider` в `providers.php`.

Доступные опции:

- `authentication.session_path` - Имя атрибута сессии, где будет храниться аутентифицированный токен.
- `authentication.remember_me.cookie_path` - Имя cookie из которой будет создаваться токен.
- `authentication.remember_me.cookie_options` - Опции cookie (lifetime, path, domain, secure, http_only)

Здесь также используются некоторые опции из `security-core-provider <https://github.com/vermillion-php/security-core-provider>`_.

Пример контроллера:

.. code-block:: php
    
    use Symfony\Component\EventDispatcher\EventDispatcherInterface as Dispatcher;
    use Symfony\Component\HttpFoundation\Request;
    use Symfony\Component\HttpFoundation\JsonResponse;
    use Symfony\Component\Security\Core\Authentication\Token\UsernamePasswordToken;
    use Symfony\Component\Security\Core\Exception\AuthenticationException;
    use Vermillion\Authentication\Events;
    use Vermillion\Authentication\SuccessEvent;
    use Vermillion\Authentication\UsernamePasswordHandler;
    
    class User
    {
    
        private $handler;
        private $dispatcher;
        private $providerKey;
    
        public function __construct(UsernamePasswordHandler $handler, Dispatcher $dispatcher, $providerKey)
        {
            $this->handler = $handler;
            $this->dispatcher = $dispatcher;
            $this->providerKey = $providerKey;
        }
    
        public function signIn(Request $request)
        {
            $returnValue = $this->handler->handle(new UsernamePasswordToken(
                trim($request->get('username', '')),
                trim($request->get('password', '')),
                $this->providerKey
            ));
            if ($returnValue instanceof UsernamePasswordToken) {
                // Dispatch success authentication event to store token in the session and cookie (if requested)
                $this->dispatcher->dispatch(
                    Events::AUTHENTICATION_SUCCESS,
                    new SuccessEvent($returnValue, (bool) $request->get('remember_me', false))
                );
                $result = ['success' => true];
            } elseif ($returnValue instanceof AuthenticationException) {
                $result = ['error' => $returnValue->getMessage()];
            } else {
                $result = ['error' => 'Authentication failed'];
            }
    
            return new JsonResponse($result);
        }
    
        public function signOut()
        {
            // Removes token from context, invalidates session and removes remember-me cookie
            $this->dispatcher->dispatch(Events::LOGOUT);
        }
    
    }


Провайдер для контроллера:

.. code-block:: php
    
    use Pimple\Container;
    use Vermillion\Api\ControllerProviderInterface;
    
    class ControllerProvider implements ControllerProviderInterface
    {
    
        public function registerControllers(Container $controllers, Container $pimple)
        {
            $controllers['user'] = function () use ($pimple) {
                return new User(
                    $pimple['authentication.handler'],
                    $pimple['dispatcher'],
                    $pimple['security.options.dao_provider_key']
                );
            };
        }
    
    }

Незабудьте добавить провайдер в `providers.php`


Отредактируйте `routing.yml`:

.. code-block:: yaml

    user.sign.in:
        path: /user/sign/in
        defaults: {_controller: user:signIn}
        requirements: {_method: POST}
    user.sing.out:
        path: /user/sign/out
        defaults: {_controller: user:signOut}

Вот, собственно, и всё.