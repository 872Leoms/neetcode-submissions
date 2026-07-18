class MinStack {
    constructor() {
         this.stack = [];
         this.minstack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if(val < this.minstack[this.minstack.length - 1] || this.minstack.length == 0){
            this.minstack.push(val);
        }else{
            this.minstack.push(this.minstack[this.minstack.length - 1]);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.stack.pop();
        this.minstack.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1]

    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minstack[this.minstack.length - 1]
    }
}
