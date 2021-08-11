class Solution:
      def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c,l = 0,len(students)
        while(c!=l):
            if(students[0]==sandwiches[0]):
                sandwiches.pop(0)
                students.pop(0)
                l = len(students)
                c=0
            else:
                k = students.pop(0)
                students.append(k)
                c+=1
        
        return l