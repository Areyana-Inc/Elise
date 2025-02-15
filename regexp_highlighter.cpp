#include "regexp_highlighter.h"
#include <QStringLiteral>

RegexpHighlighter::RegexpHighlighter(QTextDocument *parent): QSyntaxHighlighter(parent)
{

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

void RegexpHighlighter::regularExpressionChanged(const QString &text) {
    highlightRules.clear();
    QTextCharFormat keywordFormat;
    keywordFormat.setForeground(Qt::darkBlue);
    keywordFormat.setFontWeight(QFont::Bold);
    
    HightlightRule rule;

    rule.format = keywordFormat;
    rule.pattern = QRegularExpression(text);
    highlightRules.append(rule);
}
