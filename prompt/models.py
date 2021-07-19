from django.db import models

class Prompt(models.Model):
  """Prompt model"""
  content = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      """Return a string representation of a prompt"""
      return f'{self.content}'

  def as_dict(self):
      """Return a dictionary representation of a prompt"""
      return {
      'id': self.id,
      'content': self.content,
      'created_at': self.created_at,
      'updated_at': self.updated_at
      }
