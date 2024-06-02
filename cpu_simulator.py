# Portfolio Project 4
# Classes that mimic the functionalities of a CPU, cache, and memory bus

# Memory Bus Class
# Hanlde communication between the cache and the main memory
class MemoryBus:
    def __init__(self, memory_size=1024):
        self.memory = [0] * memory_size  # Simulated main memory

    def read(self, address):
        return self.memory[address]

    def write(self, address, data):
        self.memory[address] = data



# Cache Class
# Has a limited size and interacts with the memory bus for cache misses
class Cache:
    def __init__(self, memory_bus, cache_size=16):
        self.cache_size = cache_size
        self.cache = {}
        self.memory_bus = memory_bus

    def read(self, address):
        if address in self.cache:
            print(f"Cache hit at address {address}")
            return self.cache[address]
        else:
            print(f"Cache miss at address {address}")
            data = self.memory_bus.read(address)
            if len(self.cache) >= self.cache_size:
                self.evict()
            self.cache[address] = data
            return data

    def write(self, address, data):
        if len(self.cache) >= self.cache_size:
            self.evict()
        self.cache[address] = data
        self.memory_bus.write(address, data)

    def evict(self):
        evict_address = next(iter(self.cache))
        print(f"Evicting address {evict_address} from cache")
        del self.cache[evict_address]



# CPU class
# Executes basic read and write operations and interacts with the cache
class CPU:
    def __init__(self, cache):
        self.cache = cache

    def read(self, address):
        return self.cache.read(address)

    def write(self, address, data):
        self.cache.write(address, data)


# Instances of the classes
# Simulates read and write operations
def main():
    # Create a memory bus with default size
    memory_bus = MemoryBus()

    # Create a cache with the memory bus
    cache = Cache(memory_bus)

    # Create a CPU with the cache
    cpu = CPU(cache)

    # Simulate some CPU operations
    cpu.write(10, 100)  # Write 100 to address 10
    cpu.write(20, 200)  # Write 200 to address 20

    print(cpu.read(10))  # Read from address 10, should be 100
    print(cpu.read(20))  # Read from address 20, should be 200
    print(cpu.read(30))  # Read from address 30, not written, should be 0 (default)

if __name__ == "__main__":
    main()