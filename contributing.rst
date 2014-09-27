============
Содействие
============

Стандарты оформления кода
==========================

При написании кода следует придерживаться стандартов, предложенных и одобренных `группой совместимости фреймворков <http://www.php-fig.org/>`_:

- `PSR-1 <https://github.com/getjump/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md>`_
- `PSR-2 <https://github.com/getjump/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md>`_
- `PSR-4 <https://github.com/getjump/fig-standards/blob/master/accepted/PSR-4-autoloader.md>`_

В каждом проекте есть конфигурационный файл для `php-cs-fixer <http://cs.sensiolabs.org>`_, который позволяет автоматически приводить код к приведённым выше стандартам.

Тесты
=====

| Для написания unit-тестов используется `phpunit <http://phpunit.de>`_.
| Каждый проект имеет в зависимостях текущую стабильную версию phpunit.
| Таким образом, для того чтобы запустить тесты, достаточно установить все зависимости, используя `composer <http://getcomposer.org>`_ и  выполнить `vendor/bin/phpunit`.

Отправка изменений
===================

Для того, чтобы отправить ваши изменения, следует придерживаться следующего сценария:

- Сделать форк репозитория и склонировать его
- Создать тематическую ветку для необходимых изменений и переключиться в неё: `$ git checkout -b awesome-feature`
- Сделать изменения
- Написать/обновить тесты, если необходимо
- Выполнить тесты, для того, чтобы убедиться, что ничего не сломалось.
- Внести изменения в `документацию <https://github.com/vermillion-php/documentation>`_, если это необходимо
- Отправить изменения (`git push origin awesome-feature`)
- Сделать pull request

После того, как pull request был принят (или не принят), вы можете удалить ветку:

.. code-block:: sh

    $ git branch -d awesome-feature
    $ git push origin :awesome-feature

Не забудьте получить изменения из upstream перед отправкой новых изменений:

.. code-block:: sh

    $ git remote add upstream https://github.com/vermillion-php/<project_name>
    $ git checkout master
    $ git pull upstream
    $ git push origin master
