#include "mainwindow.h"

#include <QApplication>
#include <QDir>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QDir::addSearchPath("icon", QDir::currentPath() + "/theme");
      
    QFile file("dark_teal.qss");
    file.open(QFile::ReadOnly);

    QString styleSheet { file.readAll() };
    app.setStyleSheet(styleSheet);

    MainWindow w;
    w.show();
    return app.exec();
}
