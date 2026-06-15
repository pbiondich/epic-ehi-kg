# ORD_CC

> This table contains information on what users order results were CC'ed to. This information is held in the CC List (I ORD 105) item. The actual data held in the CC List item is split up into 5 separate columns. There are 5 different conditions under which a value can be added to the CC List item. It is possible, when CC'ing a result, to select a single user, a pool, a class, enter an ad hoc recipient, and also to note a recipient to exclude. Each different category is split out to a different column for the purpose of networking.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CC_LIST_USER_ID` | VARCHAR |  | This column displays the recipient user ID if appropriate. This column is linked to the identifier item (EMP .1) of the User (EMP) master file. |
| 4 | `CC_LIST_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `CC_LIST_POOL_ID` | NUMERIC |  | This column displays pool record ID for the recipient if appropriate. This column is linked to the identifier item (HIP .1) of the Registry (HIP) master file. |
| 6 | `CC_LIST_POOL_ID_REGISTRY_NAME` | VARCHAR |  | The name of the In Basket registry in the HIP master file. |
| 7 | `CC_LIST_CLASS_ID` | VARCHAR |  | This column displays the class recipient if appropriate. This column is linked to the classifications item (EMP-450) in the User (EMP) master file. |
| 8 | `CC_LIST_ADHOC` | VARCHAR |  | This column displays the ad hoc recipient if appropriate. |
| 9 | `CC_LIST_EX_USER_ID` | VARCHAR |  | This column displays the excluded user ID for the recipient if appropriate. This column is linked to the identifier item (EMP .1) of the User (EMP) master file. |
| 10 | `CC_LIST_EX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

