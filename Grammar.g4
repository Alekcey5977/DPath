grammar Grammar;


// Входная точка языка
query: pathExpr;

// Путь состоит из шагов, разделённых '::/'
pathExpr: SLASH step (SLASH step)*;

// Шаг пути: ось и идентификатор
step: axis identifier? | identifier;

// Оси (направления поиска)
axis: ('child'
    | 'descendant'
    | 'descendant_or_self'
    | 'parent'
    | 'ancestor'
    | 'ancestor_or_self'
    | 'following'
    | 'following_sibling'
    | 'preceding'
    | 'preceding_sibling') '::/';

// Идентификатор (имя AVP)
identifier: IDENTIFIER;
SLASH: '/';
// Терминалы
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_.]*; // Алфавитные символы, подчёркивания и цифры

// Пропускаем пробелы
WS: [ \t\r\n]+ -> skip;

