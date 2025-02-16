#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "regexp_highlighter.h"

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
private slots: 
    void matchesChanged(const QList<QRegularExpressionMatch> matches);
    void helpTriggered();
    void infoTriggered();

private:
    void setupSignals();

private:
    Ui::MainWindow *ui;
    RegexpHighlighter *highlighter;
};
#endif // MAINWINDOW_H
