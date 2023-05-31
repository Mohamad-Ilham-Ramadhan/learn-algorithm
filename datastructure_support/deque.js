class Deque {
   constructor() {
     this.items = {};
     this.frontIndex = 0;
     this.endIndex = 1;
     this.size = 0;
   }
 
   // Add an element to the front of the deque
   addFront(element) {
     this.items[this.frontIndex] = element;
     // this.endIndex = this.frontIndex === 0 && this.endIndex === 0 ? 1 : this.endIndex;
     this.frontIndex--;
     this.size++;
   }
 
   // Add an element to the rear of the deque
   addRear(element) {
     this.items[this.endIndex] = element;
     // this.frontIndex = this.endIndex === 0 && this.frontIndex === 0 ? -1 : this.frontIndex;
     this.endIndex++;
     this.size++;
   }
 
   // Remove and return the element from the front of the deque
   removeFront() {
     if (this.isEmpty()) {
       return null;
     }
     const front = this.items[this.frontIndex + 1];
     delete this.items[this.frontIndex + 1];
     this.frontIndex++;
     this.size--;
     return front;
   }
 
   // Remove and return the element from the rear of the deque
   removeRear() {
     if (this.isEmpty()) {
       return null;
     }
     const end = this.items[this.endIndex - 1];
     delete this.items[this.endIndex - 1];
     this.endIndex--;
     this.size--;
     return end;  
   }
 
   // Return the element at the front of the deque without removing it
   peekFront() {
     if (this.isEmpty()) {
       return null;
     }
     return this.items[this.frontIndex + 1];
   }
 
   // Return the element at the rear of the deque without removing it
   peekRear() {
     if (this.isEmpty()) {
       return null;
     }
     return this.items[this.endIndex - 1];
   }
 
   // Check if the deque is empty
   isEmpty() {
     return this.size === 0;
   }
 
   // Return the size of the deque
 
   // Clear the deque
   clear() {
     this.items = {};
     this.frontIndex = 0;
     this.endIndex = 0;
     this.size = 0;
   }
 }