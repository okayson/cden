# cden

## Requirements

* cd$B$N8zN(2=(B
	* $B0\F0MzNr$rI=<((B->$BA*Br$7$F0\F02DG=$H$9$k(B
	* `.`$B$rF~NO$7$?$i!"%+%l%s%H%G%#%l%/%H%j0J2<$rI=<((B->$BA*Br$7$F0\F02DG=$H$9$k(B

* $B0\F0MzNr$N4IM}(B
	* cd$B$NETEY!"0\F0@h(B+$B0\F02s?t$r5-O?$9$k(B
	* $B5-O??t$K$O:GBg?t$r@_$1$k(B
	* $B5-O??t$N>e8B$KC#$7$?>l9g$O0\F02s?t$N>/$J$$$b$N$+$i:o=|$9$k(B
	* home$B$X$N0\F0!"(B..$B$G$N0\F0(B(?)$B!"%+%l%s%H%G%#%l%/%H%j$X$N0\F0$O4IM}BP>]$H$7$J$$(B

* $B0\F0MzNr$NI=<((B
	* $B@hF,$K$O(Bhome$B$rI=<($9$k(B(cd + enter$B$G(Bhome$B$K0\F0$G$-$k$h$&$K(B)
	* $B8=:_$N%Q%9$r4^$`%Q%9$r@hF,$KI=<($9$k(B
	* $B8=:_$N2<0L%G%#%l%/%H%j$rI=<($9$k!J;~4V$,$+$+$k$+$b!"(B./$B$HF~NO$7$?$i!"$H$+$N$[$&$,NI$$$+$b(B) 

## Implementaton notes

* $B@dBP%Q%9$G5-O?$9$k(B
* symbolic link$B$O$=$N$^$^5-O?$9$k(B

## Name candidate
* acceleratedcd
* accelcd
* accd

## Note
```shell
function ac(){
	# $1 : empty	=> $BMzNr$+$i8uJd$rI=<((B
	#	 : .		=> CurrentDir$B$+$i8uJd$rI=<((B
	#	 : <dir>	=> $B2?$b$7$J$$(B
	dir = accd.py $1
	if [ -n "$1" ]; then
		accd.py
	elif
		accd.py $1
	else
		cd $1
	fi
}
```

