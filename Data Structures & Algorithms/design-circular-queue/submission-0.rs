struct MyCircularQueue {
    size: usize,
    index: usize,
    quene: Vec<i32>,
}

impl MyCircularQueue {
    pub fn new(k: i32) -> Self {
        Self {
            size: 0,
            index: 0,
            quene: vec![0; k as usize],
        }
    }

    pub fn en_queue(&mut self, value: i32) -> bool {
        if self.is_full() {
            return false;
        }

        let position = (self.index + self.size) % self.quene.len();
        self.quene[position] = value;
        self.size += 1;
        true
    }

    pub fn de_queue(&mut self) -> bool {
        if self.is_empty() {
            return false;
        }

        self.index = (self.index + 1) % self.quene.len();
        self.size -= 1;
        true
    }

    pub fn front(&self) -> i32 {
        if self.is_empty() {
            return -1;
        }

        self.quene[self.index]
    }

    pub fn rear(&self) -> i32 {
        if self.is_empty() {
            return -1;
        }

        let position = (self.index + self.size - 1) % self.quene.len();
        self.quene[position]
    }

    pub fn is_empty(&self) -> bool {
        self.size == 0
    }

    pub fn is_full(&self) -> bool {
        self.size == self.quene.len()
    }
}