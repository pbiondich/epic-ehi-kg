# MC_PRICER_LCD_INFO

> This table stores information about LCD evaluation results from the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the pricer message record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ARTICLE_LCD_CHECK_RESULT_C_NAME` | VARCHAR |  | The LCD evaluation result from the CMS article stored in ARTICLE_LCD_IDENT. |
| 4 | `ARTICLE_LCD_IDENT` | VARCHAR |  | The ID of a CMS LCD article evaluated by the Epic Pricer. |
| 5 | `ARTICLE_LCD_VERSION` | VARCHAR |  | The CMS version of the article in ARTICLE_LCD_IDENT used by the Epic Pricer to run LCD checks. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

