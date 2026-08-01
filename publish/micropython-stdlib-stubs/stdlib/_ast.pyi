import sys
from ast import (
    AST as AST,
)
from ast import (
    Add as Add,
)
from ast import (
    And as And,
)
from ast import (
    AnnAssign as AnnAssign,
)
from ast import (
    Assert as Assert,
)
from ast import (
    Assign as Assign,
)
from ast import (
    AsyncFor as AsyncFor,
)
from ast import (
    AsyncFunctionDef as AsyncFunctionDef,
)
from ast import (
    AsyncWith as AsyncWith,
)
from ast import (
    Attribute as Attribute,
)
from ast import (
    AugAssign as AugAssign,
)
from ast import (
    Await as Await,
)
from ast import (
    BinOp as BinOp,
)
from ast import (
    BitAnd as BitAnd,
)
from ast import (
    BitOr as BitOr,
)
from ast import (
    BitXor as BitXor,
)
from ast import (
    BoolOp as BoolOp,
)
from ast import (
    Break as Break,
)
from ast import (
    Call as Call,
)
from ast import (
    ClassDef as ClassDef,
)
from ast import (
    Compare as Compare,
)
from ast import (
    Constant as Constant,
)
from ast import (
    Continue as Continue,
)
from ast import (
    Del as Del,
)
from ast import (
    Delete as Delete,
)
from ast import (
    Dict as Dict,
)
from ast import (
    DictComp as DictComp,
)
from ast import (
    Div as Div,
)
from ast import (
    Eq as Eq,
)
from ast import (
    ExceptHandler as ExceptHandler,
)
from ast import (
    Expr as Expr,
)
from ast import (
    Expression as Expression,
)
from ast import (
    FloorDiv as FloorDiv,
)
from ast import (
    For as For,
)
from ast import (
    FormattedValue as FormattedValue,
)
from ast import (
    FunctionDef as FunctionDef,
)
from ast import (
    FunctionType as FunctionType,
)
from ast import (
    GeneratorExp as GeneratorExp,
)
from ast import (
    Global as Global,
)
from ast import (
    Gt as Gt,
)
from ast import (
    GtE as GtE,
)
from ast import (
    If as If,
)
from ast import (
    IfExp as IfExp,
)
from ast import (
    Import as Import,
)
from ast import (
    ImportFrom as ImportFrom,
)
from ast import (
    In as In,
)
from ast import (
    Interactive as Interactive,
)
from ast import (
    Invert as Invert,
)
from ast import (
    Is as Is,
)
from ast import (
    IsNot as IsNot,
)
from ast import (
    JoinedStr as JoinedStr,
)
from ast import (
    Lambda as Lambda,
)
from ast import (
    List as List,
)
from ast import (
    ListComp as ListComp,
)
from ast import (
    Load as Load,
)
from ast import (
    LShift as LShift,
)
from ast import (
    Lt as Lt,
)
from ast import (
    LtE as LtE,
)
from ast import (
    MatMult as MatMult,
)
from ast import (
    Mod as Mod,
)
from ast import (
    Module as Module,
)
from ast import (
    Mult as Mult,
)
from ast import (
    Name as Name,
)
from ast import (
    NamedExpr as NamedExpr,
)
from ast import (
    Nonlocal as Nonlocal,
)
from ast import (
    Not as Not,
)
from ast import (
    NotEq as NotEq,
)
from ast import (
    NotIn as NotIn,
)
from ast import (
    Or as Or,
)
from ast import (
    Pass as Pass,
)
from ast import (
    Pow as Pow,
)
from ast import (
    Raise as Raise,
)
from ast import (
    Return as Return,
)
from ast import (
    RShift as RShift,
)
from ast import (
    Set as Set,
)
from ast import (
    SetComp as SetComp,
)
from ast import (
    Slice as Slice,
)
from ast import (
    Starred as Starred,
)
from ast import (
    Store as Store,
)
from ast import (
    Sub as Sub,
)
from ast import (
    Subscript as Subscript,
)
from ast import (
    Try as Try,
)
from ast import (
    Tuple as Tuple,
)
from ast import (
    TypeIgnore as TypeIgnore,
)
from ast import (
    UAdd as UAdd,
)
from ast import (
    UnaryOp as UnaryOp,
)
from ast import (
    USub as USub,
)
from ast import (
    While as While,
)
from ast import (
    With as With,
)
from ast import (
    Yield as Yield,
)
from ast import (
    YieldFrom as YieldFrom,
)
from ast import (
    alias as alias,
)
from ast import (
    arg as arg,
)
from ast import (
    arguments as arguments,
)
from ast import (
    boolop as boolop,
)
from ast import (
    cmpop as cmpop,
)
from ast import (
    comprehension as comprehension,
)
from ast import (
    excepthandler as excepthandler,
)
from ast import (
    expr as expr,
)
from ast import (
    expr_context as expr_context,
)
from ast import (
    keyword as keyword,
)
from ast import (
    mod as mod,
)
from ast import (
    operator as operator,
)
from ast import (
    stmt as stmt,
)
from ast import (
    type_ignore as type_ignore,
)
from ast import (
    unaryop as unaryop,
)
from ast import (
    withitem as withitem,
)
from typing import Literal

if sys.version_info >= (3, 12):
    from ast import ParamSpec as ParamSpec
    from ast import TypeVar as TypeVar
    from ast import TypeVarTuple as TypeVarTuple
    from ast import type_param as type_param

if sys.version_info >= (3, 11):
    pass

if sys.version_info >= (3, 10):
    from ast import (
        MatchAs as MatchAs,
    )
    from ast import (
        MatchClass as MatchClass,
    )
    from ast import (
        MatchMapping as MatchMapping,
    )
    from ast import (
        MatchOr as MatchOr,
    )
    from ast import (
        MatchSequence as MatchSequence,
    )
    from ast import (
        MatchSingleton as MatchSingleton,
    )
    from ast import (
        MatchStar as MatchStar,
    )
    from ast import (
        MatchValue as MatchValue,
    )
    from ast import (
        match_case as match_case,
    )
    from ast import (
        pattern as pattern,
    )

if sys.version_info < (3, 9):
    from ast import (
        AugLoad as AugLoad,
    )
    from ast import (
        AugStore as AugStore,
    )
    from ast import (
        ExtSlice as ExtSlice,
    )
    from ast import (
        Index as Index,
    )
    from ast import (
        Param as Param,
    )
    from ast import (
        Suite as Suite,
    )
    from ast import (
        slice as slice,
    )

PyCF_ALLOW_TOP_LEVEL_AWAIT: Literal[8192]
PyCF_ONLY_AST: Literal[1024]
PyCF_TYPE_COMMENTS: Literal[4096]

if sys.version_info >= (3, 13):
    PyCF_OPTIMIZED_AST: Literal[33792]
