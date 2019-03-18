class CreateTodoItems < ActiveRecord::Migration
  def change
    create_table :todo_items do |t|
      t.string :title
      t.text :description
      t.date :due_date
      t.boolean :completed

      t.timestamps null: false
    end
  end
end
