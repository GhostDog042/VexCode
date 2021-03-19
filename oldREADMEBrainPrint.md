# VexCode

Welcome to my VexCode backups! Fair warning, some of this code may be mildly inexplicable.

## INVENTORY

* Clawbot Remote Print V5 (**BORKED**)
  * __SHOULD__ print motor speeds to the brain screen, but has some weird error.
  * ___TO DO___
  * [X] Figure out the error
   * VexCode can't converd variable outputs directly into strings
  * [X] Fix the code
  * [X] Figure out why the heck this program keeps throwing errors whenever `brain.screen.print()` is involved
   * `brain.screen.print` is fine, printing directly from things like `motor.velocity(PERCENT)` is illegal
  * [X] Commit edits to the main branch 
* Clawbot Remote Basic V5 
  *  Allows for remote driving. No muss, no fuss.
*  V5 Claw For
	*  Draws a hex-eight
*  V5 Claw Motor-Sensor
	*  Basic motor-sensor setup for a V5 Clawbot. This is used as a template for most of the other files here to save time
