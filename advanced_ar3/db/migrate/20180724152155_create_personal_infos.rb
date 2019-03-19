class CreatePersonalInfos < ActiveRecord::Migration
  def change
    create_table :personal_infos do |t|
      t.float :height
      t.float :weight
      t.references :person, index: true, forign_key: true
      t.string :references

      t.timestamps null: false
    end
  end
end
