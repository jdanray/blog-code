(defun hanoi (n src dest spare)
  (if (= n 0)
    nil
    (append (hanoi (1- n) src spare dest)
            (list (list 'move 'ring n 'from src 'to dest))
            (hanoi (1- n) spare dest src))))

(hanoi 3 'src 'dest 'spare)
