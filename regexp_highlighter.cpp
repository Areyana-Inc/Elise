#include "regexp_highlighter.h"
#include <QStringLiteral>

RegexpHighlighter::RegexpHighlighter(QTextDocument *parent): QSyntaxHighlighter(parent)
{
    regexFormat.setForeground(Qt::darkBlue);
    regexFormat.setFontWeight(QFont::Bold);
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
    
    HightlightRule rule;

    rule.format = regexFormat;
    rule.pattern = QRegularExpression(text);
    highlightRules.append(rule);
    rehighlight();
}
