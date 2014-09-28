Console
=======

Обёртка для `Symfony/Console <http://symfony.com/doc/current/components/console/introduction.html>`_.

Установка
---------

.. code-block:: sh

    $ composer require vermillion/console
    
Использование
-------------

Создать файл `bin/console`:

.. code-block:: php

    #!/usr/bin/env php
    <?php
    
    require __DIR__ . '/../vendor/autoload.php';
    
    (new \Vermillion\Console\Application(__DIR__))
        ->setName('vermillion')
        ->setVersion('1.0.0')
        ->run(true);

Сделать его исполняемым:

.. code-block:: sh
    
    $ chmod +x bin/console



Конструктор класса `\\Vermillion\\Console\\Application` принимает два аргумента. 

Первый - путь к директорию с конфигами, второй (опциональный) - экземпляр класса `\\Pimple\\Container`.
 
В директории с конфигами обязательно должен быть файл `providers.php`, который возвращает массив доступных провайдеров.


Пример:

.. code-block:: php
    
    <?php
    //providers.php
    
    return [
        '\\CommandProvider',
        '\\ServiceProvider' => [
            'options' => [/* ... */],
            'another_option' => 'value',
        ],
    ];
    

Опции можно указывать только для провайдеров, реализующих `\\Pimple\\ServiceProviderInterface`.


Методы `setName()` и `setVersion()` устанавливают имя и версию приложения.

Метод `run($interactive = false, InputInterface $in = null, OutputInterface $out = null)` - запускает приложение.
 
Аргумент `$interactive` позволяет запусить шелл.
 
Аргументы `$in` и `$out` - экземпляры классов, реализующих `\\Symfony\\Component\\Console\\Input\\InputInterface` и `\\Symfony\\Component\\Console\\Output\\OutputInterface`.

При запуске шелла изменение значений аргументов не будет иметь никакого эффекта.

Добавление команд
~~~~~~~~~~~~~~~~~~

Для того, чтобы добавить команду в приложение, вам необходимо создать для неё провайдер и добавить его в `providers.php`

Пример:

.. code-block:: php

    use Pimple\Container;
    use Symfony\Component\Console\Command\Command;
    use Vermillion\Console\CommandProviderInterface;

    class CommandProvider implements CommandProviderInterface
    {

        public function registerCommands(Container $commands, Container $pimple)
        {
            $commands['command'] = function () {
                return new Command('demo');
            };
        }
    
    }
    
Имя, под которым зарегистрирована команда в контейнере, не имеет никакого специального назначения.

Для более подробной информации обратитесь к документации `компонента <http://symfony.com/doc/current/components/console/introduction.html>`_ и `Pimple <https://github.com/fabpot/Pimple>`_.
