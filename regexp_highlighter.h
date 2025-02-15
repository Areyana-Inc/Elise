#ifndef REGEXP_HIGHLIGHTER_H
#define REGEXP_HIGHLIGHTER_H

#include <QSyntaxHighlighter>
#include <QRegularExpression>

class RegexpHighlighter: public QSyntaxHighlighter 
{
    Q_OBJECT
public:
    RegexpHighlighter(QTextDocument *parent = nullptr);
protected:
    void highlightBlock(const QString &text) override;
public slots:
    void regularExpressionChanged(const QString &text);
signals:
    void highlightUpdated();

private:
    struct HightlightRule
    {
        QRegularExpression pattern;
        QTextCharFormat format;
    };
    QList<HightlightRule> highlightRules;
};

#endif // REGEXP_HIGHLIGHTER_H
