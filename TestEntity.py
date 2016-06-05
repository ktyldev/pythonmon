import unittest
from Entity import Entity

class Test_TestEntity(unittest.TestCase):

    def test_move_position_no_children(self):        
        entity = Entity('testEntity', '', 1)
        
        entity.move_position(10, 10)
        
        self.assertEqual(entity.x, 10)
        self.assertEqual(entity.y, 10)
    def test_move_position_one_child(self):
        entity = Entity('testEntity', '', 0, 0)
        
        entity.child_entities.append(Entity('', '', 1))
        entity.move_position(10, 10)
        
        self.assertEqual(entity.child_entities[0].x, 10)
        self.assertEqual(entity.child_entities[0].y, 10)
    def test_move_position_one_child_offset(self):
        entity = Entity('testEntity', '', 0, 0)

        entity.child_entities.append(Entity('', '', 1, 10, 10))
        entity.move_position(10, 10)
        
        self.assertEqual(entity.child_entities[0].x, 20)
        self.assertEqual(entity.child_entities[0].y, 20)

if __name__ == '__main__':
    unittest.main()
