class TodoItem < ActiveRecord::Base

  def numCompleted
    TodoItem.all.count
  end
end
