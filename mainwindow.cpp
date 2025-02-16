#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "regexp_highlighter.h"
#include <QSyntaxHighlighter>
#include <QRegularExpressionValidator>
#include <QRegularExpression>
#include <QStandardItemModel>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    highlighter = new RegexpHighlighter(ui->testStringTextEdit->document());

    setupSignals();
}

void MainWindow::setupSignals() 
{
    connect(ui->regularExpressionEdit, &QLineEdit::textChanged, highlighter, &RegexpHighlighter::regularExpressionChanged);
    connect(highlighter, &RegexpHighlighter::highlightUpdated, this, &MainWindow::matchesChanged);
    
    //Menu
    connect(ui->actionHelp, &QAction::triggered, this, &MainWindow::helpTriggered);
    connect(ui->actionInfo, &QAction::triggered, this, &MainWindow::infoTriggered);
}

void MainWindow::helpTriggered()
{
    QMessageBox msgBox;
    msgBox.setText("Help triggered. REPLACE TEXT.");
    msgBox.exec();
}

void MainWindow::infoTriggered()
{
    QMessageBox msgBox;
    msgBox.setText("Info triggered. REPLACE TEXT");
    msgBox.exec();
}

void MainWindow::matchesChanged(const QList<QRegularExpressionMatch> matches)
{
    auto matchList = ui->matchList;
    auto itemModel = new QStandardItemModel();

    for (qsizetype i = 0; i < matches.size(); ++i) {
        auto currentMatch = matches[i];
        auto line = QString("Match %1 - %2 : %3").arg(currentMatch.capturedStart()).arg(currentMatch.capturedEnd()).arg(currentMatch.captured());
        auto item = new QStandardItem(line);
        itemModel->appendRow(item);
    }

    matchList->setModel(itemModel);
}

MainWindow::~MainWindow()
{
    delete ui;
}
