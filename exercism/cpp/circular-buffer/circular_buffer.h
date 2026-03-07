#pragma once

#include <vector>
#include <stdexcept>

namespace circular_buffer {

template <typename T>
class circular_buffer {
private:
    std::vector<T> buffer_;
    size_t capacity_;
    size_t read_pos_;
    size_t write_pos_;
    size_t size_;

public:
    explicit circular_buffer(size_t capacity);
    
    T read();
    void write(const T& value);
    void overwrite(const T& value);
    void clear();
};

template <typename T>
circular_buffer<T>::circular_buffer(size_t capacity)
    : buffer_(capacity), capacity_(capacity), read_pos_(0), write_pos_(0), size_(0) {}

template <typename T>
T circular_buffer<T>::read() {
    if (size_ == 0) {
        throw std::domain_error("Buffer is empty");
    }
    
    T value = buffer_[read_pos_];
    read_pos_ = (read_pos_ + 1) % capacity_;
    --size_;
    return value;
}

template <typename T>
void circular_buffer<T>::write(const T& value) {
    if (size_ == capacity_) {
        throw std::domain_error("Buffer is full");
    }
    
    buffer_[write_pos_] = value;
    write_pos_ = (write_pos_ + 1) % capacity_;
    ++size_;
}

template <typename T>
void circular_buffer<T>::overwrite(const T& value) {
    if (size_ == capacity_) {
        buffer_[write_pos_] = value;
        write_pos_ = (write_pos_ + 1) % capacity_;
        read_pos_ = (read_pos_ + 1) % capacity_;
    } else {
        write(value);
    }
}

template <typename T>
void circular_buffer<T>::clear() {
    read_pos_ = 0;
    write_pos_ = 0;
    size_ = 0;
}

}  // namespace circular_buffer
