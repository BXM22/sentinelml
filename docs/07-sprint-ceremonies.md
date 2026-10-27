# Sprint ceremonies and templates

A solo developer keeps the rituals short; the point is a written goal, a written result and one lesson each week.

| Ceremony | When | Length | Output |
| --- | --- | --- | --- |
| Sprint planning | Sunday or Monday start | 30 min | Sprint goal and chosen stories |
| Daily check-in | Each work session | 5 min | One line: done, next, blocked |
| Sprint review | Last day | 20 min | Demo of the working increment and metrics |
| Retrospective | After review | 15 min | Keep, stop, try list |

## Definition of ready

A story may enter a sprint when:

- It has a one-sentence goal and written acceptance criteria
- Its data source is identified and reachable
- It fits in about 3 points or less

## Definition of done

A story is finished when:

- Code is merged to `main` through a pull request
- Tests and security scans pass
- Metrics are recorded in `reports/`
- The README or changelog reflects the change

## Daily check-in template

```markdown
Date:
Done:
Next:
Blocked:
```

## Retrospective template

```markdown
Sprint N: goal met? (yes / partly / no)
Points planned vs. completed:
Keep doing:
Stop doing:
Try next sprint:
One thing I learned about ML or security:
```
