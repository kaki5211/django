chcp 65001
set /P x="コメント　>> "

cd C:\Users\katsuki\Desktop\arikui_blog\django
git add .
git commit -m "%x%"
git push proj1 master