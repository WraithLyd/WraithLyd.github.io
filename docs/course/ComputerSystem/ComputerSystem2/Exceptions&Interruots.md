### Handler Action
+ read cause, and transfer to relevant handler
+ determine action required
+ If restartable:
    + take corrective action
    + use SEPC to return to program
+ Otherwise:
    + terminate program
    + report error using SEPC, etc.

### Exceptions in a pipeline
+ another form of control hazard
+ consider malfunction on add in EX stage `add x1, x2, x1`


## Software-Hardware Interface