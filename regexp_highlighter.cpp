#include "regexp_highlighter.h"
#include <QStringLiteral>

RegexpHighlighter::RegexpHighlighter(QTextDocument *parent): QSyntaxHighlighter(parent)
{
    HightlightRule rule;

    QString testReg = QStringLiteral("\\bchar\\b");
    QTextCharFormat keywordFormat;
    keywordFormat.setForeground(Qt::darkBlue);
    keywordFormat.setFontWeight(QFont::Bold);
    rule.format = keywordFormat;
    rule.pattern = QRegularExpression(testReg);
    highlightRules.append(rule);
}

void RegexpHighlighter::highlightBlock(const QString &text)
{
    for (const HightlightRule &rule : std::as_const(highlightRules)) {
        QRegularExpressionMatchIterator matchIterator = rule.pattern.globalMatch(text);
        while (matchIterator.hasNext()) {
            QRegularExpressionMatch match = matchIterator.next();
            setFormat(match.capturedStart(), match.capturedLength(), rule.format);
        }
    }
}
