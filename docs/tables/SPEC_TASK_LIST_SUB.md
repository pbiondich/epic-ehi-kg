# SPEC_TASK_LIST_SUB

> This is sub container information for Anatomic Pathology specimens.

**Primary key:** `SPECIMEN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique ID of the specimen record |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the sub container information for anatomic pathology (AP) specimens. Together with SPECIMEN_ID, this forms the foreign key for this table, SPEC_TASK_LIST. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of specific sub container information for anatomic pathology (AP) specimens associated with the different tasks on the specimen from the SPEC_TASK_LIST table. |
| 4 | `TASK_LINKED_SCTR_ID` | VARCHAR |  | Stores a container designation that may be created in association with a specific container and task, as in a slide for a given block designation with a specific stain. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

