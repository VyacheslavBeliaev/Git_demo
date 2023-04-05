#  команды Git
# $ git init - инициализируем репозиторий гит
# git add . (,main.py или другие файлы) добавляем файлы
# git status проаеряем статус
# git commit -m 'Messaage сообщение' добавляем код/файлы в локальный репозиторий
# git config --global user.email "vbelyaev86@gmail.com" / требует авторизации, надо добавить свою почту
# git config --global user.name "Vyacheslav Beliaev" / надо добавить свое имя
# *** git add . и git commit - делаем всегда кгда внесли в файлы изменения! ***
# git log
# git branch feature  / создаем новую ветку
# git checkout feature / master / переключаемся на другую ветку
# git merge feature / соединяем обе ветки master и feature
# *** Делали локально ***
#
# *** Делаем на удаленном репозитории ***
#
#
# $ git remote add origin https: // github.com / VyacheslavBeliaev / Git_demo.git   - присоединяем удаленный репозиторий гит
# $ git remote -v присоединили локадльный с удаленным
# git status
# git push origin main
# git branch -m master main - переименовываем ветку репозитория (была master) должна быть одинакового названия (main и локалльно и на удаленном репозитории (сайт)
# git pull origin main --allow-unrelated-histories -подключаем Readme.md
# git fetch origin main
#  git push origin main - подключаемся к Git
#
# git restore --staged file_1exp.py - если надо отменить добавление или что-то
#  git gui - если работать не в коммандной строке