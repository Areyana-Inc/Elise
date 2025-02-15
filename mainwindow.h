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
public slots: 
    void matchesChanged(const QList<QRegularExpressionMatch> matches);

private:
    Ui::MainWindow *ui;
    RegexpHighlighter *highlighter;
};
#endif // MAINWINDOW_H
