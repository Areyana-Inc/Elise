#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "regexp_highlighter.h"
#include <QSyntaxHighlighter>
#include <QRegularExpressionValidator>
#include <QRegularExpression>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    highlighter = new RegexpHighlighter(ui->testStringTextEdit->document());
    
}

MainWindow::~MainWindow()
{
    delete ui;
}
