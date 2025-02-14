#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QSyntaxHighlighter>
#include <QRegularExpressionValidator>
#include <QRegularExpression>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QRegularExpression re("[0-9 ]+");
    QRegularExpressionValidator validator(re);
    
}

MainWindow::~MainWindow()
{
    delete ui;
}
